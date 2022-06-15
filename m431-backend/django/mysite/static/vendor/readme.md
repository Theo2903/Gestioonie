# install dependencies
npm install

# build for development
npx tailwindcss build -i styles.css -o ../css/style.css

# build for production (purge unused style)
npx tailwindcss --purge build -i styles.css -o ../css/style.css 

