# API Automation Testing Framework

This is an API automation testing framework built with Python, Pytest, and Allure Report, employing OOP (Object-Oriented Programming) and Client Pattern design.

---

## Execution Commands

### Standard Execution Workflow

It is recommended to clear old results before each execution to ensure report accuracy:

```bash
# 1. Clear old records, execute tests, generate new records
rm -rf allure-results/* && pytest -v --alluredir=allure-results

# 2. Open graphical test report (automatically opens in browser)
allure serve allure-results

```

### Useful Supplementary Commands

* **Install necessary packages:**
```bash
pip install requests pytest allure-pytest

```


* **Generate static report folder (without starting Server):**
```bash
allure generate allure-results -o allure-report --clean

```


* **Execute tests for a specific module:**
```bash
pytest test_case/product_type/ -v --alluredir=allure-results

```



---

## Framework Architecture Description

This framework uses a layered design to improve code reusability:

### 1. Base Layer (`api_requests/base.py`)

* **Core Function:** Encapsulates `requests` methods.
* **Processing Logic:**
* Uniformly manages headers and Authorization.
* Implements the `_send_request` private method to handle URL joining and Allure step recording.
* Provides public interfaces such as `get`, `post`, `put`, and `delete`.



### 2. Client Layer (`api_requests/xxx_client.py`)

* **Core Function:** Inherits from `BaseAPI` and is encapsulated for different functional modules (e.g., Product, Reservation).
* **Advantages:** Encapsulates API Endpoints and specific parameters within classes; test scripts do not need to directly touch URLs, conforming to encapsulation principles.

### 3. Test Case Layer (`test_case/`)

* **Core Function:** Writing test cases and Assertions.
* **Execution Logic:** Injects Client objects through Fixtures provided by `conftest.py`, focusing on verifying API response fields and `msg_code` business logic.

---

## Project Structure 


graph TD
    %% 定義樣式
    classDef base fill:#f9f,stroke:#333,stroke-width:2px;
    classDef client fill:#ccf,stroke:#333,stroke-width:1px;
    classDef test fill:#ff9,stroke:#333,stroke-width:1px;
    classDef config fill:#ddd,stroke:#333,stroke-width:1px,stroke-dasharray: 5 5;

    %% 核心層級
    subgraph Layer3_Test_Cases [Test Case Layer (test_case/)]
        TC_PT[test_get_list_of_product_type.py]
        TC_Res[test_get_reservation_availability.py]
        TC_Tax[test_get_tax_group_list.py]
    end

    subgraph Layer2_Clients [Client Layer (api_requests/)]
        CL_PT[Product_TypeClient.py]
        CL_Res[Reservation_AvailabilityClient.py]
        CL_Tax[TaxationClient.py]
    end

    subgraph Layer1_Base [Base Layer (api_requests/base.py)]
        BaseAPI((BaseAPI Class))
    end

    %% 配置與 Fixtures
    subgraph Configuration
        CONF[conftest.py <br/> (Pytest Fixtures)]
        ENV[.env <br/> (BaseURL, Tokens)]
    end

    %% 外部依賴
    RequestsLib[requests Library]
    AllureLib[allure-pytest Library]

    %% 關聯線
    %% 繼承關係
    CL_PT -.->|Inherits| BaseAPI
    CL_Res -.->|Inherits| BaseAPI
    CL_Tax -.->|Inherits| BaseAPI

    %% 調用與注入關係
    CONF -->|Reads| ENV
    CONF -->|Instantiates| CL_PT
    CONF -->|Instantiates| CL_Res
    CONF -->|Instantiates| CL_Tax

    TC_PT -->|Uses Fixture| CL_PT
    TC_Res -->|Uses Fixture| CL_Res
    TC_Tax -->|Uses Fixture| CL_Tax

    %% 底層依賴
    BaseAPI ==>|Uses| RequestsLib
    BaseAPI ==>|Integrates| AllureLib

    %% 應用樣式
    class BaseAPI base;
    class CL_PT,CL_Res,CL_Tax client;
    class TC_PT,TC_Res,TC_Tax test;
    class CONF,ENV config;



api_testing/
├── api_requests/               # API Client Layer (OOP)
│   ├── base.py                 # Base API class with core request logic
│   ├── product_type/
│   │   └── Product_TypeClient.py
│   ├── reservation_availability/
│   │   └── Reservation_AvailabilityClient.py
│   ├── service_call/
│   │   └── Service_CallClient.py
│   └── taxation/
│   │    └── TaxationClient.py
│   │ 
│   │         
│   ├── TBD/
│   
├── test_case/                  # Test Case Layer
│   ├── product_type/
│   │   
│   ├── reservation_availability/
│   │   
│   ├── service_call/
│   │   
│   └── taxation/
│   │         
│   ├── TBD/
│   
├── allure-results/             # Temporary folder for test results (JSON)
├── venv/                       # Python Virtual Environment
├── conftest.py                 # Pytest shared fixtures
├── .env                        # Environment variables (Base URL, Tokens)
├── .gitignore                  # Git ignore rules (pycache, allure-results)
└── README.md                   # Project documentation

---

## Environment Requirements

* **Python**: 3.13+
* **Allure CLI**: Requires installation of system-level tools (macOS: `brew install allure`)