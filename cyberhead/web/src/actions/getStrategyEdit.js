import API_BASE from './URL'

async function getStrategyEdit(name){
	let response = await fetch(`${API_BASE}/get_strategy_edit/${name}`)
	let data = await response.json()
	return data
}


export default getStrategyEdit;