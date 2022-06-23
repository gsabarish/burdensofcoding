FROM mongo

COPY init.json /init.json
CMD mongoimport --host db --db test --collection test --type json --file /init.json --jsonArray