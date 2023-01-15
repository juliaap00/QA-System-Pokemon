from pokemon_qa import qa

'''queries = ["¿Qué número de la pokedex es Charizard?"
		,"¿En qué entrada de la pokedex se encuentra Charizard?"
		,"¿Con que número se puede identificar a Charizard?"
		,"¿Cómo se puede describir a Charizard?"
		,"¿Cómo está descrito Charizard en la pokedex?"
		,"¿Cómo es Charizard?"
		,"¿Cuál es el tipo de Charizard?"
		,"¿Qué tipo potencia Charizard?"
		,"¿Con que tipo hace más daño Charizard?"
		,"¿Qué afecta mucho a Charizard?"
		,"¿Con que se debilita a Charizard?"
		,"¿Qué evita Charizard para no herirse?"
		,"¿Cuánto pesa Charizard?"
		,"¿Es Charizard pesado?"
		,"¿Cuan alto es Charizard?"
		,"¿Es muy grande Charizard?"
		,"¿Es Charizard un pokemon legendario?"
		,"¿Es Charizard mitológico?"
		,"¿Cómo de único es Charizard?"
		,"¿Tiene Charizard alguna pasiva?"
		,"¿Cuáles son las habilidades de Charizard?"
		,"¿Qué características son propias de Charizard?"
		,"¿Qué habilidades dificiles de conseguir tiene Charizard?"
		,"¿Tiene algunas habilidades especiales Charizard ?"
		,"¿Qué características ocultas tiene Charizard?"
		,"¿Cuándo apareció Charizard?"
		,"¿En qué generación se introdujo a Charizard?"
		,"¿En qué juego apareció Charizard?"
		,"¿Dónde vive el pokemon Charizard?"
		,"¿Cuál es el hábitat de los pokemon como Charizard?"
		,"¿Dónde nacen y viven los Charizard?"
		,"¿Tiene alguna evolución Charizard?"
		,"¿Que preevoluciones tiene Charizard?"
		,"¿Que cadena evolutiva tiene Charizard?"
		,"¿Dónde se obtiene a Charizard?"
		,"¿Cómo capturar a Charizard?"
		,"¿Dónde se puede conseguir a Charizard?"
		,"¿Qué valor tiene el ratio de captura de Charizard?"
		,"¿Cómo de difícil es capturar a Charizard?"
		,"¿Es muy probable capturar a Charizard?"
		,"¿Cuáles son los ataques que aprende Charizard?"
		,"¿Que movimientos puede hacer Charizard?"
		,"¿Cuáles son los movimientos que puede aprender Charizard?"
		]
'''

queries = ["¿Cuánto pesa Charizard?",
"Como de pesado es Charizard",
"¿Cuántos kilos pesa Charizard?",
"Cual es el peso de Charizard",
"Como de pesado es Charizard"]

for query in queries:
	print(">>>", query)
	print(qa(query))
	print()
	print("----------------------------------------------------------------------------------------")
