<p> The <bold>AI Emergency First Aid Guide</bold> is a web-based intelligent system designed to provide step-by-step first aid guidance during emergency situations. The system leverages ,<bold>Retrieval-Augmented Generation (RAG)</bold>, semantic search, and rule-based safety intelligence to assist users in critical moments. </p>

<p> Key Features </p>
<ul>
<li>Text-based emergency description </li>
<li>Voice-based emergency input</li>
<li>Image-based injury detection using a medical image classifier</li>
</ul>

<p> Steps to Run locally </p>
<ul>
<li>  Clone this repository </li>
<li>  Create a virtual environment <code> python -m venv venv </code> </li>
<li>  Activate the virtual environment, Mac: <code> source venv/bin/activate </code> , Windows: <code> venv\Scripts\activate </code> </li>
<li>  Install the requirements using <code> pip install -r requirements.txt </code> </li>
<li>  To initialize the vector store, run the following command in your terminal: <code>python backend/embedding\_engine.py</code> </li>

</ul> 