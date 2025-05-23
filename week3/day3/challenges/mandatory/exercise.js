      const systemeSolaire = [
                { nom: "Mercure", couleur: "#808080", distance: 100, vitesse: 4.15, info: "Plus petite planète", lunes: [] },
                { nom: "Vénus", couleur: "#FFA500", distance: 150, vitesse: 1.62, info: "Planète la plus chaude", lunes: [] },
                { nom: "Terre", couleur: "#0000FF", distance: 200, vitesse: 1, info: "Notre maison", lunes: [{ nom: "Lune" }] },
                { nom: "Mars", couleur: "#FF0000", distance: 250, vitesse: 0.53, info: "Planète rouge", lunes: [{ nom: "Phobos" }, { nom: "Deimos" }] },
                { nom: "Jupiter", couleur: "#FFA07A", distance: 350, vitesse: 0.084, info: "Plus grande planète", lunes: [{ nom: "Io" }, { nom: "Europe" }, { nom: "Ganymède" }, { nom: "Callisto" }] },
                { nom: "Saturne", couleur: "#FFD700", distance: 450, vitesse: 0.034, info: "Anneaux célèbres", lunes: [{ nom: "Titan" }, { nom: "Encelade" }, { nom: "Mimas" }] },
                { nom: "Uranus", couleur: "#00CED1", distance: 550, vitesse: 0.012, info: "Planète inclinée", lunes: [{ nom: "Titania" }, { nom: "Obéron" }] },
                { nom: "Neptune", couleur: "#00008B", distance: 650, vitesse: 0.006, info: "Vents puissants", lunes: [{ nom: "Triton" }] }
            ];

            const sectionPlanetes = document.querySelector(".listPlanets");
            let time = 0;

            systemeSolaire.forEach((planete) => {
                // Création de la planète
                const divPlanete = document.createElement("div");
                divPlanete.classList.add("planet");
                divPlanete.style.backgroundColor = planete.couleur;
                divPlanete.textContent = planete.nom;

                // Création de l'info-bulle
                const infoDiv = document.createElement("div");
                infoDiv.classList.add("info");
                infoDiv.textContent = planete.info;
                divPlanete.appendChild(infoDiv);

                // Affichage de l'info au survol
                divPlanete.addEventListener("mouseover", () => infoDiv.style.display = "block");
                divPlanete.addEventListener("mouseout", () => infoDiv.style.display = "none");

                // Ajout des lunes
                planete.lunes.forEach((lune, indexLune) => {
                    const divLune = document.createElement("div");
                    divLune.classList.add("moon");
                    divLune.textContent = lune.nom;
                    divLune.style.animation = `orbitMoon ${5 + indexLune}s linear infinite`;
                    divPlanete.appendChild(divLune);
                });

                sectionPlanetes.appendChild(divPlanete);
            });

            // Animation du système solaire
            function animateSolarSystem() {
                time += 0.01;
                const planets = document.querySelectorAll(".planet");
                
                systemeSolaire.forEach((planete, index) => {
                    const angle = time * planete.vitesse;
                    const x = window.innerWidth / 2 + Math.cos(angle) * planete.distance;
                    const y = window.innerHeight / 2 + Math.sin(angle) * planete.distance;
                    
                    planets[index].style.left = `${x - 50}px`; // -50 pour centrer
                    planets[index].style.top = `${y - 50}px`;
                    
                    // Position de l'info-bulle
                    planets[index].querySelector(".info").style.top = "-40px";
                    planets[index].querySelector(".info").style.left = "50%";
                    planets[index].querySelector(".info").style.transform = "translateX(-50%)";
                });

                requestAnimationFrame(animateSolarSystem);
            }
            animateSolarSystem();