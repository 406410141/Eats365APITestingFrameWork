# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /Testing

# 3. Install system dependencies (Java is required for Allure Report)
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-jre \
    wget \
    && rm -rf /var/lib/apt/lists/*

# 4. Install Allure Commandline Tool
RUN wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz && \
    tar -zxvf allure-2.24.0.tgz -C /opt/ && \
    ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure && \
    rm allure-2.24.0.tgz

# 5. Copy the dependency list and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the entire project source code
COPY . .

# 7. Grant execution permissions to the reporting script
RUN chmod +x /Testing/run_and_report.sh

# 8. Expose the port for the web report server
EXPOSE 8070

# 9. Use the script as the entry point to run tests and serve the report
ENTRYPOINT ["/bin/bash", "/Testing/run_and_report.sh"]