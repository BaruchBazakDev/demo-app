db.getSiblingDB("employees");
db.devops.drop();

db.devops.insertMany([
    {
        "id": 1,
        "f_name": "Baruch",
        "l_name": "Bazak",
        "city": "Tel-Mond",
        "address": "azofit",
        "phone_number": "054-399-7477"
    },
    {
        "id": 2,
        "f_name": "Tom",
        "l_name": "Brovender",
        "city": "Herzelya",
        "address": "DC",
        "phone_number": "054-459-7477"
    },
    {
        "id": 3,
        "f_name": "Amit",
        "l_name": "Zarmon",
        "city": "Mevaseret",
        "address": "aahaghgd",
        "phone_number": "054-319-7477"
    },
]);