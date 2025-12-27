<p> The <strong>AI Emergency First Aid Guide</strong> is a web-based intelligent system designed to provide step-by-step first aid guidance during emergency situations. The system leverages ,<strong>Retrieval-Augmented Generation (RAG)</strong>, semantic search, and rule-based safety intelligence to assist users in critical moments. </p>

<p> Key Features </p>
<ul>
<li>Text-based emergency description </li>
<li>Voice-based emergency input</li>
<li>Image-based injury detection using a medical image classifier</li>
<li>Emergency category classification (Trauma, Cardiac, Neurological, etc.)</li>
<li>Severity level estimation (Low / Medium / High / Critical)</li>
<li>“What NOT to Do” safety guidance.</li>
<li>Emergency Readiness Checklist</li>
<li>Emergency Timeline Tips (time-critical awareness)</li>
<li>Emergency Quick Call panel with regional emergency numbers.</li>
<li>Stores past emergency queries and responses.</li>
</ul>

<p> Steps to Run locally </p>
<ul>
<li>  Clone this repository </li>
<li>  Create a virtual environment <code> python -m venv venv </code> </li>
<li>  Activate the virtual environment, Mac: <code> source venv/bin/activate </code> , Windows: <code> venv\Scripts\activate </code> </li>
<li>  Install the requirements using <code> pip install -r requirements.txt </code> </li>
<li>  To initialize the vector store, run the following command in your terminal: <code>python backend/embedding\_engine.py</code> </li>
<li>  Run the application using <code> streamlit run app.py </code>

</ul> 
