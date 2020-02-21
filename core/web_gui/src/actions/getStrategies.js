async function getStrategies(strategy){
	let response = await fetch(`http://localhost:5000/get_strategies`)
	let data = await response.json()
	return data
}


export default getStrategies;