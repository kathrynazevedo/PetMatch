document.addEventListener("DOMContentLoaded", function() {
    const btnAdotante = document.getElementById("adotante");
    const btnTutor = document.getElementById("tutor");

    if (btnAdotante && btnTutor) {
        btnAdotante.addEventListener("click", function() {
            btnAdotante.classList.add("selected");
            btnTutor.classList.remove("selected");
        });

        btnTutor.addEventListener("click", function() {
            btnTutor.classList.add("selected");
            btnAdotante.classList.remove("selected");
        });
    }

    const cadAdotante = document.getElementById("cad-adotante");
    const cadTutor = document.getElementById("cad-tutor");

    if (cadAdotante && cadTutor) {
        cadAdotante.addEventListener("click", function() {
            cadAdotante.classList.add("selected");
            cadTutor.classList.remove("selected");
        });

        cadTutor.addEventListener("click", function() {
            cadTutor.classList.add("selected");
            cadAdotante.classList.remove("selected");
        });
    }

    // Dados dos pets
    const pets = [
        { 
            nome: "Raiza", 
            imagem: "https://images.amigonaosecompra.com.br/unsafe/0x0/753c0df8-b45e-46fc-95ea-cd318a75462e/73b555fa-2e7f-46a7-b4cd-8067ed5644d8/73b555fa-2e7f-46a7-b4cd-8067ed5644d8.jpg?v=63909102544", 
            info: "Cachorro | Fêmea | Adulto | Porte médio",
            raca: "SRD", 
            vacinacao: "Vacinada", 
            localizacao: "São Paulo - SP" 
        },
        { 
            nome: "Athena", 
            imagem: "https://images.amigonaosecompra.com.br/unsafe/0x0/b3093993-80d1-4014-b70c-ace5471c4fd6/e58797e8-e1d9-4b88-9fe4-8c9d1f59aab9/e58797e8-e1d9-4b88-9fe4-8c9d1f59aab9.jpeg?v=63909113655", 
            info: "Cachorro | Fêmea | Adulto | Porte pequeno",
            raca: "Poodle", 
            vacinacao: "Vacinada e vermifugada", 
            localizacao: "Rio de Janeiro - RJ" 
        },
        { 
            nome: "Pingo", 
            imagem: "https://images.amigonaosecompra.com.br/unsafe/0x0/b3093993-80d1-4014-b70c-ace5471c4fd6/7ec27990-8b51-4acc-a5c2-4da5f4f38350/7ec27990-8b51-4acc-a5c2-4da5f4f38350.jpeg?v=63907938386", 
            info: "Gato | Macho | Filhote | Porte pequeno",
            raca: "Persa", 
            vacinacao: "Vacinado", 
            localizacao: "Belo Horizonte - MG" 
        },
        { 
            nome: "Doritos", 
            imagem: "https://images.amigonaosecompra.com.br/unsafe/0x0/86f45627-25db-49a8-8119-7bd68511e3f3/383f3d3e-7796-4da4-abf3-be36fcb5ed05/383f3d3e-7796-4da4-abf3-be36fcb5ed05.jpg?v=63909050126", 
            info: "Cachorro | Macho | Filhote | Porte médio",
            raca: "Golden Retriever", 
            vacinacao: "Vacinado e castrado", 
            localizacao: "Curitiba - PR" 
        },
        { 
            nome: "Sophie", 
            imagem: "https://images.amigonaosecompra.com.br/unsafe/0x0/86f45627-25db-49a8-8119-7bd68511e3f3/999c75bc-4c2a-4213-8711-01bb27ad1cdd/999c75bc-4c2a-4213-8711-01bb27ad1cdd.jpg?v=63908871152", 
            info: "Gato | Fêmea | Adulto | Porte médio",
            raca: "Siamesa", 
            vacinacao: "Vacinada e castrada", 
            localizacao: "Porto Alegre - RS" 
        }
    ];

    const petsContainer = document.getElementById("petsContainer");

    pets.forEach(pet => {
        let petCard = document.createElement("div");
        petCard.classList.add("pet-card");
        petCard.innerHTML = `
            <img src="${pet.imagem}" alt="${pet.nome}">
            <h3>${pet.nome}</h3>
            <p class="adoption-info">${pet.info}</p>
            <p><strong>Raça:</strong> ${pet.raca}</p>
            <p><strong>Vacinação:</strong> ${pet.vacinacao}</p>
            <p><strong>Localização:</strong> ${pet.localizacao}</p>
            <button class="adoption-button" onclick="showModal()">DISPONÍVEL</button>
        `;
        petsContainer.appendChild(petCard);
    });

    function showModal() {
        document.getElementById("confirmModal").classList.add("active");
        document.getElementById("overlay").classList.add("active");
    }

    function closeModal() {
        document.getElementById("confirmModal").classList.remove("active");
        document.getElementById("overlay").classList.remove("active");
    }

    function showTutorInfo() {
        closeModal();
        document.getElementById("tutorInfo").classList.add("active");
    }

    function closeTutorInfo() {
        document.getElementById("tutorInfo").classList.remove("active");
    }
});
