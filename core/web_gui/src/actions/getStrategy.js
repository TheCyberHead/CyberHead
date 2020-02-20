async function getStrategy(strategy){
	let response = await fetch(`http://localhost:5000/get_strategy/${strategy}`)
	let data = await response.json()
	return data
}


export default getStrategy;