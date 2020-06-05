import API_BASE from './URL'

async function getHeatMaps(){
	let response = await fetch(`${API_BASE}/heatmap`)
	let data = await response.json()
	return data
}


export default getHeatMaps;