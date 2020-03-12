import API_BASE from './URL'

async function getStrategy(strategy){
	let response = await fetch(`${API_BASE}/get_strategy/${strategy}`)
	let data = await response.json()
	return data
}


export default getStrategy;