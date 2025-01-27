from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(text1, text2):
    """Calculate the cosine similarity between two strings."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

if __name__ == "__main__":
    text1 = input("Enter the first string: ")
    text2 = input("Enter the second string: ")
    similarity = calculate_cosine_similarity(text1, text2)
    print(f"Cosine Similarity: {similarity:.4f}")
