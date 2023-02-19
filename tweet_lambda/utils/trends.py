
import random

trends = [
    "AI and ML",
    "Natural Language Processing",
    "Blockchain",
    "Cryptocurrency",
    "Edge Computing",
    "Cloud Computing",
    "5G Technology",
    "Cybersecurity",
    "Quantum Computing",
    "Virtual Reality",
    "Augmented Reality",
    "Big Data",
    "Cloud-native Computing",
    "Serverless Computing",
    "Digital Twin",
    "Federated Learning",
    "Autonomous Vehicles",
    "Chatbots",
    "Collaborative Robots",
    "Computer Vision",
    "Data Visualization",
    "Digital Ecosystems",
    "Drones",
    "Generative AI",
    "Graph Databases",
    "Haptic Feedback",
    "Open-source Software",
    "Explainable AI (XAI)",
    "Internet of Medical Things (IoMT)",
    "Intelligent Process Automation (IPA)",
    "Spatial Computing",
    "Quantum Machine Learning",
    "Explainable Blockchain",
    "Synthetic Data Generation",
    "Internet of Energy (IoE)",
    "Digital Ethics and Governance",
    "Blockchain Interoperability",
    "Algorithmic Bias Detection and Mitigation",
    "Distributed Cloud Computing",
    "Neurotechnology",
    "Synthetic Biology",
    "Augmented Humanity",
    "Neuromorphic Computing",
    "Explainable Robotics",
    "Smart Dust",
    "Multi-cloud Computing",
    "Immersive Technology",
    "Natural User Interfaces (NUI)",
    "Biometric Authentication",
    "Smart Grid Technology",
    "Decentralized Autonomous Organizations (DAO)",
    "Cyber-Physical Systems (CPS)",
    "Ethical AI",
    "Machine Learning Ops (MLOps)",
    "Autonomous IoT Devices",
    "Fog Computing",
    "Software-Defined Networking (SDN)",
    "Swarm Intelligence"
]


def get_trend(count=1):
    """ Get random trend
    """
    randint = random.randint(0, len(trends) - 1)
    return trends[randint]