import API_BASE from './URL'

async function getStrategies(strategy){
	let response = await fetch(`${API_BASE}/get_strategies`)
	let data = await response.json()
	return data
}


export default getStrategies;