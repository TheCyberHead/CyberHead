import API_BASE from './URL'

async function getHeatMapData(id){
	let response = await fetch(`${API_BASE}/heatmap/${id}`)
	let data = await response.json()
	return data
}


export default getHeatMapData;