# RAG Application with OpenAI Chat, Embedders, and CoinGecko API

This repository hosts a real-time streaming analytics and AI application powered by Pathway, OpenAI, and CoinGecko's BTC exchange rates API. Leveraging Pathway's Python data processing framework, developers can seamlessly orchestrate analytics and AI pipelines tailored for streaming data, ensuring optimal performance in dynamic environments. Pathway's intuitive Python API abstracts away complexities like late data and consistency management, enabling developers to focus on building engaging and insightful applications. 

Powered by OpenAI's language models, the application delivers immersive conversational experiences, while CoinGecko's BTC exchange rates API provides users with up-to-date insights into cryptocurrency markets. By combining these cutting-edge technologies, the repository offers a unified platform for real-time streaming analytics and AI, empowering users with actionable insights and engaging interactions.

## Key Features
- Real-time streaming analytics and AI powered by Pathway.
- Engaging conversational experiences with OpenAI's language models.
- Up-to-date cryptocurrency market insights with CoinGecko's BTC exchange rates API.
- Scalable Rust engine based on Differential Dataflow for efficient incremental computation.
- Seamless integration with Python ML libraries for enhanced analytical capabilities.

This repository provides a comprehensive framework for building real-time streaming applications with advanced analytics and AI capabilities. Whether you're a developer, researcher, or enthusiast, this project offers a powerful toolkit for creating innovative streaming solutions.

## Run with Docker

1. **Create `.env` file:**
   - Create a `.env` file in the root directory of the project.
   - Copy and paste the below configuration into the `.env` file.
   - Replace the placeholders with your actual values:
     ```
     OPENAI_API_TOKEN={YOUR_OPENAI_API_KEY}
     EMBEDDER_LOCATOR=text-embedding-ada-002
     EMBEDDING_DIMENSION=1536
     MODEL_LOCATOR=gpt-3.5-turbo
     MAX_TOKENS=200
     TEMPERATURE=0.0
     HOST=0.0.0.0
     PORT=8080
     ```
2. **Build with Docker Compose:**
   - From the project root folder, open your terminal.
   - Run the following command to build the Docker image:
     ```
     docker compose build
     ```
3. **Run with Docker Compose:**
   - After the build is successful, run the following command to start the application:
     ```
     docker compose up
     ```
4. **Access the Application:**
   - Once Docker installation is successful, navigate to [localhost:8501](http://localhost:8501) on your browser.

## Demo Video
https://github.com/tripathiprash/btc-exchange-rates-chat/assets/90844054/b47ecedb-2cbe-442c-8528-58d654baea8e

### Description:
This app is particularly useful for cryptocurrency traders, investors, financial analysts, business owners, developers, and tech enthusiasts. Cryptocurrency traders and investors benefit from real-time exchange rates and market trends, enabling them to make informed trading decisions and manage risks effectively. Financial analysts and advisors can leverage personalized insights and market sentiment analysis to offer better investment advice. Additionally, the capabilities of OpenAI Chat allow users to interact with the application conversationally, making it easier to obtain insights without the need to visit and search multiple websites. This enhances user experience by providing immediate, tailored responses and comprehensive information through a simple chat interface.

## Dockerfile CMD
In the Dockerfile, the following command is used to start the application:
```dockerfile
CMD ["bash", "-c", "python3 main.py & streamlit run app.py"]
```

## Copy Updated JSONL File from Docker Container to Local Computer
To save a copy of the updated JSONL file from the Docker container to your local computer, use the following command:
```bash
docker cp {container_name}:/app/examples/data/exchange_rates.jsonl /path/to/local/directory

