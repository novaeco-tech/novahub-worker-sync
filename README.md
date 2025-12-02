# 🌫️ NovaAir Worker: Air Quality

> **The Atmospheric Translator.**
> Real-time ingestion, normalization, and AQI calculation for the ecosystem's air monitoring network.

[](https://www.google.com/search?q=https://github.com/novaeco-tech/novaair-worker-air-quality/actions)
[](https://opensource.org/licenses/MIT)
[](https://www.google.com/search?q=https://quality.air.novaeco.tech)

**AirQuality** is a headless, stream-processing worker belonging to the **[NovaAir](https://www.google.com/search?q=https://air.novaeco.tech)** sector.

Raw sensor data is meaningless to a human. A reading of `0x4F` from a particulate sensor does not tell a city planner if the air is safe. This worker bridges the gap between hardware (`NovaInfra`) and policy (`NovaPolicy`). It ingests raw telemetry, applies calibration curves, calculates standard indices (EU CAQI / US AQI), and flags violation events.

-----

## 🎯 Value Proposition

Air is a shared common resource. To manage it (and monetize its improvement via credits), we need trusted data.

1.  **Standardization:** Transforms proprietary data formats from 50+ sensor manufacturers (Bosch, Sensirion, Honeywell) into a unified NovaEco Air Schema.
2.  **Health Safety:** Instantly calculates the **Air Quality Index (AQI)**. If PM2.5 spikes above safe limits, it triggers immediate alerts to `NovaHealth`.
3.  **Credit Verification:** Provides the verified "Proof of Clean Air" required for **NovaTrade** to mint Environmental Impact Bonds or Carbon Removal Credits.

-----

## 🏗️ Architecture (The Data Pipeline)

This worker consumes the `queue.air.quality-readings` queue managed by NovaAir.

```mermaid
graph LR
    subgraph "The Physical Layer (NovaInfra)"
        Station[Monitoring Station] -->|MQTT Payload| MQ[(RabbitMQ)]
        Drone[NovaAir Drone] -->|MQTT Payload| MQ
    end

    subgraph "The Worker (NovaAir)"
        MQ -->|1. Ingest Reading| Worker[Air Quality Worker]
        Worker -->|2. Apply Calibration| Calib[Drift Correction Model]
        Worker -->|3. Calculate AQI| Math[AQI Algorithms]
    end

    subgraph "Downstream"
        Worker -->|4. Time-Series Data| DB[(NovaAir DB)]
        Worker -->|5. Hazard Alert| Policy[NovaPolicy]
        Worker -->|6. Mint Credit| Trade[NovaTrade]
    end
```

### The Processing Lifecycle

1.  **Ingest:** Receives a normalized sensor payload from `NovaInfra`.
      * *Example:* `{"sensor_id": "AIR-BER-09", "type": "PM2.5", "raw_value": 35.4, "unit": "ug/m3"}`.
2.  **Calibration:** Applies machine-learning based "Drift Correction." Low-cost sensors drift over time due to humidity/temperature. This worker corrects the value using reference station data (Virtual Reference).
3.  **Calculation:** Converts the raw concentration (µg/m³) into an Index Score (0-500) based on local regulations (EU vs US standards).
4.  **Thresholding:**
      * *Green:* Store data.
      * *Red:* Trigger `HazardEvent` to **NovaPolicy** (e.g., "Factory X exceeded emissions limit").

-----

## ✨ Key Features

### 1\. Multi-Pollutant Normalization

It handles the "Big 5" criteria pollutants seamlessly:

  * **Particulate Matter:** PM1.0, PM2.5, PM10.
  * **Gases:** NO₂ (Nitrogen Dioxide), SO₂ (Sulfur Dioxide), O₃ (Ozone), CO (Carbon Monoxide).
  * **Volatiles:** VOCs (Volatile Organic Compounds) for indoor safety.

### 2\. "Virtual Reference" Calibration

Cheap sensors are inaccurate. This worker uses a **Fleet Learning** algorithm.

  * If 50 cheap sensors in a neighborhood report "High Pollution" but the expensive Reference Station reports "Low," the worker detects the discrepancy.
  * It dynamically adjusts the calibration factor for the cheap sensors based on humidity/temperature correlation logic.

### 3\. Impact Credit Generation

If a reforestation project in **NovaNature** successfully lowers local temperature and PM2.5 levels over 1 year, this worker aggregates that delta and sends a "Verified Outcome" to **NovaTrade** to unlock payment.

-----

## 🚀 Getting Started

### Prerequisites

  * Docker Desktop
  * Python 3.11+ (NumPy/Pandas for vector math)

### Installation

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/novaeco-tech/novaair-worker-air-quality.git
    cd novaair-worker-air-quality
    ```
2.  **Start the Dev Environment:**
    ```bash
    make dev
    ```
      * Starts the worker.
      * Starts a mock data generator (simulating a smog event).
      * **Health Check:** `http://localhost:8080/health`

### Configuration (`.env`)

```ini
# Queue
RABBITMQ_URI=amqp://guest:guest@rabbitmq:5672/
QUEUE_NAME=queue.air.quality-readings

# Standards Configuration
AQI_STANDARD=EU_CAQI # Options: US_EPA, CN_HJ, EU_CAQI
ALERT_THRESHOLD_PM25=25.0 # ug/m3

# Integrations
NOVAPOLICY_URL=http://novapolicy-api:8000
```

-----

## 📂 Repository Structure

```text
novaair-worker-air-quality/
├── src/
│   ├── main.py             # Consumer Loop
│   ├── algorithms/         # AQI conversion formulas (EPA/EU)
│   ├── calibration/        # Humidity/Temp correction logic
│   └── models/             # Pydantic schemas for Pollution Events
├── tests/                  # Pytest suite
└── Dockerfile              # Python runtime
```

-----

## 🧪 Testing

We use **Scenario-Based Testing**.

  * **Math Tests:** `make test-algo`
      * Verifies that `35.4 ug/m3` of PM2.5 correctly converts to `AQI 100` under EPA standards.
  * **Alert Tests:** `make test-alert`
      * Injects a "Toxic Spike" event and asserts that the worker emits a high-priority message to `NovaPolicy`.

-----

## 🤝 Contributing

We need contributors with expertise in **Atmospheric Science**, **IoT Data Science**, and **Public Health Standards**.
See [CONTRIBUTING.md](https://www.google.com/search?q=../.github/CONTRIBUTING.md) for details.

**Maintainers:** `@novaeco-tech/maintainers-sector-novaair`