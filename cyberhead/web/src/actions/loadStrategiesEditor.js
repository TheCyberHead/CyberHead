import API_BASE from './URL'

async function loadStrategiesEditor(){
	let response = await fetch(`${API_BASE}/get_strategies_edit`)
	let data = await response.json()
	return data
}


export default loadStrategiesEditor;