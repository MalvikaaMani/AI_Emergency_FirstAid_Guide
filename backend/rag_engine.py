import faiss
import numpy as np
from backend.llm_engine import LLMEngine
from .utils import get_sentence_embedder


class RAGEngine:
    def __init__(self):
        # Load cached sentence embedder
        self.embedder = get_sentence_embedder()

        # Load FAISS index and corpus
        self.index = faiss.read_index("vector_store/firstaid_index.bin")
        self.corpus = np.load("vector_store/corpus.npy", allow_pickle=True)

        # Initialize LLM engine
        self.llm = LLMEngine()

        # Similarity threshold (lower = stricter match)
        self.similarity_threshold = 1.2

    # -------------------------------
    # Semantic search
    # -------------------------------
    def search_context(self, user_query):
        query_embedding = self.embedder.encode([user_query])
        distances, indices = self.index.search(query_embedding, k=1)

        distance = distances[0][0]
        context = self.corpus[indices[0][0]]

        return distance, context

    # -------------------------------
    # Prompt for known emergencies
    # -------------------------------
    def build_rag_prompt(self, context, user_query):
        return f"""
Use ONLY the steps from the context.

Context:
{context}

User emergency:
{user_query}

TASK:
Output ONLY the numbered steps.
Each step on a new line.

End with:
Call emergency services immediately.
"""

    # -------------------------------
    # Prompt for unknown emergencies
    # -------------------------------
    def build_safety_warning_prompt(self, user_query):
        return f"""
Strict Instruction: You are an AI First Aid System.

The user has requested guidance for an unknown emergency:
"{user_query}"

You are strictly forbidden from providing any first aid steps.

Output ONLY the following sentence:
Call emergency services immediately (911/999/000) and seek professional medical help. Do not wait.
"""

    # -------------------------------
    # ORIGINAL METHOD (unchanged)
    # -------------------------------
    def get_response(self, user_query):
        distance, context = self.search_context(user_query)

        if distance < self.similarity_threshold:
            prompt = self.build_rag_prompt(context, user_query)
        else:
            prompt = self.build_safety_warning_prompt(user_query)

        return self.llm.generate_answer(prompt)

    # -------------------------------
    # NEW METHOD (for extended app)
    # -------------------------------
    def get_response_with_meta(self, user_query):
        """
        Returns:
        - response text
        - metadata dictionary (category, method)
        """

        distance, context = self.search_context(user_query)

        if distance < self.similarity_threshold:
            prompt = self.build_rag_prompt(context, user_query)
            method = "RAG"

            # Extract scenario name safely
            if "Scenario:" in context:
                category = context.split("Scenario:")[1].split("\n")[0].strip()
            else:
                category = "Known Emergency"

        else:
            prompt = self.build_safety_warning_prompt(user_query)
            method = "Fallback"
            category = "Unknown"

        response = self.llm.generate_answer(prompt)

        return response, {
            "category": category,
            "method": method,
            "similarity_distance": round(float(distance), 3)
        }
