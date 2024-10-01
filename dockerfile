# Utilise l'image Python 3.9 comme base
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Mettre à jour pip
RUN pip install --upgrade pip

# Copier le fichier requirements.txt dans le répertoire de travail du conteneur
COPY requirements.txt .

# Installer les dépendances Python listées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application dans le conteneur
COPY . .

WORKDIR /app/2024-frontend


# Mettez à jour le système et installez les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    libpq-dev \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Accédez au répertoire frontend et installez les dépendances Node.js
RUN npm install

WORKDIR /app

# Exposer le port sur lequel Django va écouter
EXPOSE 8000

# Commande pour lancer l'application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]