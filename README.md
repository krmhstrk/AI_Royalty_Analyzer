# 🎵 AI-Powered Royalty Analyzer
# 🎵 AI-Powered Royalty Analyzer

## 🎯 Project Purpose

This project demonstrates an AI-driven system designed to automate and streamline critical processes within music royalty management. The core objectives include:

1.  **Automated Data Extraction:** Leveraging Natural Language Processing (NLP) to automatically extract key information from complex licensing agreements (e.g., royalty rates, payment terms, territorial rights, minimum guarantees).
2.  **Discrepancy Identification:** Implementing mechanisms to help identify potential inconsistencies or anomalies within royalty reports by comparing reported data against contractual terms or historical patterns.
3.  **Revenue Forecasting & Trend Analysis:** Structuring extracted and reported data to facilitate the analysis of revenue trends and enable more accurate financial forecasting.
4.  **Automated Reporting:** Generating summarized insights and visualizations through a simple dashboard to support data-driven decision-making for stakeholders.

## 🛠️ Technologies Demonstrated (Conceptual & Implemented)

This project utilizes and demonstrates the following technologies:

* **Python:** As the primary programming language for scripting and data manipulation.
* **(Conceptual) OpenAI API (e.g., GPT models):** For advanced document analysis (contract parsing). This part is simulated in the Colab notebook using mock responses to showcase the intended functionality without live API calls.
* **Google Colab:** As the development and demonstration environment for the Python-based contract data extraction script (`Contract_Extractor_AI_Royalty.ipynb`).
* **Pandas:** For structuring and analyzing data within Python (used in both Colab and Streamlit).
* **Streamlit:** For building the simple, interactive web dashboard (`royalty_dashboard.py`) for data visualization and insights.
* **Plotly Express:** For generating interactive charts within the Streamlit dashboard.
* **CSV:** As the data format for sample royalty reports (`sample_royalty_data.csv`).

## 📂 System Components & Workflow

The system consists of the following key components:

1.  **Contract Data Extraction (`Contract_Extractor_AI_Royalty.ipynb`):**
    * A Google Colab notebook designed to simulate the extraction of key terms (royalty rates, payment periods, minimum guarantees, territorial rights, special conditions) from license agreement texts.
    * **Workflow:**
        * A sample contract text is provided within the notebook.
        * The notebook uses predefined "prompts" (questions/instructions).
        * A simulation function (`get_simulated_contract_info`) returns mock (predefined) structured data, mimicking the output an AI model like OpenAI's GPT would generate in response to these prompts.
        * The extracted (mock) information is then displayed.
    * **Note:** This component demonstrates the AI data extraction concept. In a production system, it would involve secure API calls to a live AI model.

2.  **Interactive Royalty Dashboard (`royalty_dashboard.py` & `sample_royalty_data.csv`):**
    * A web-based dashboard built with Streamlit.
    * **Workflow:**
        * The dashboard loads royalty report data from a CSV file (either uploaded by the user or using the provided `sample_royalty_data.csv` by default). This CSV data is assumed to be the output of prior processing (e.g., data extracted from publisher reports and potentially reconciled with contract terms).
        * It displays summary metrics (total revenues, discrepancies).
        * It provides interactive visualizations (bar charts, pie charts) of revenue by song, discrepancies, and revenue by royalty type using Plotly Express.
        * Users can filter the data by song title and royalty type.
        * The UI supports English and German.

## 🚀 How to Use

### 1. Contract Data Extraction (Google Colab Notebook)
    1. Open the `Contract_Extractor_AI_Royalty.ipynb` file in Google Colab.
    2. You can review the sample contract text and the mock responses defined within the notebook.
    3. Select "Runtime" from the menu and then "Run all".
    4. The notebook will execute all cells, and the simulated extracted information will be printed below the final code cell.
    5. **Note:** No API keys are required for this demonstration as it uses mock data.

### 2. Interactive Royalty Dashboard (Streamlit)
    1. Ensure you have Python installed on your system.
    2. Install the required libraries:
       ```bash
       pip install streamlit pandas plotly
       ```
    3. Download (or clone) the `royalty_dashboard.py` script and the `sample_royalty_data.csv` file to the same directory on your computer.
    4. Open your Terminal or Command Prompt, navigate to that directory.
    5. Run the Streamlit app using the command:
       ```bash
       streamlit run royalty_dashboard.py
       ```
    6. Your web browser should automatically open to the dashboard. You can upload a different CSV (with the same column structure) or use the default sample data.

*(Optional: You can add a screenshot of your Streamlit dashboard here later by uploading an image to your GitHub repo and linking it: ![Dashboard Screenshot](link_to_your_dashboard_screenshot.png))*

## 📈 Business Value Demonstration (Conceptual)

This AI-driven system, if fully implemented, could offer substantial business value to a music company:

* **Increased Efficiency:**
    * Automating the extraction of key terms from lengthy contracts can reduce manual effort by an estimated **60-80%**.
    * Streamlining the initial review of royalty reports against contractual terms can significantly speed up the reconciliation process.
* **Error Reduction:**
    * Minimizing human error in data entry and interpretation from contracts and reports can lead to more accurate royalty calculations and payments, potentially reducing costly mistakes by **30-50%**.
* **Enhanced Revenue Assurance:**
    * Systematic comparison of expected vs. reported/paid amounts can help identify underpayments or missed revenue streams more effectively.
    * Improved accuracy in royalty processing contributes to better cash flow management.
* **Data-Driven Insights:**
    * The dashboard provides quick visualizations of revenue trends, discrepancies, and performance by song or royalty type, enabling faster and more informed strategic decisions.
* **Scalability:**
    * An automated system can handle a growing volume of contracts and royalty statements with greater ease than purely manual processes.

## 🔮 Future Enhancements

* **Live AI Integration:** Replace mock responses in the Colab notebook with actual calls to an OpenAI API (or similar LLM) for real-time contract analysis, including secure API key management.
* **Direct Database Integration:** Connect the system to internal databases for fetching contract terms and royalty data, and for storing AI-extracted information.
* **Advanced Discrepancy Detection:** Implement more sophisticated algorithms (e.g., statistical analysis, machine learning) to flag subtle anomalies in royalty reports.
* **Automated Report Generation:** Extend the dashboard to generate exportable PDF or Excel summary reports for stakeholders.
* **User Authentication & Roles:** For a production system, implement user accounts and role-based access control.
* **Expanded Language Support:** Train or fine-tune AI models to handle contracts in multiple languages more effectively.

## 👤 About the Creator

This project was conceptualized and developed by **[Adın Soyadın]** as a portfolio piece to demonstrate capabilities in AI-driven business process automation and data analysis.
* **LinkedIn:** [LinkedIn Profilinin Linki]
* **GitHub:** [GitHub Profilinin Linki (örneğin: https://github.com/krmhstrk)]

---

*This is a portfolio project showcasing an automation-first approach to solving challenges in the music industry.*
