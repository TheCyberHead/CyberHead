import API_BASE from './URL'

async function getDatasets(){
	let response = await fetch(`${API_BASE}/datasets`)
	let data = await response.json()
	return data
}


export default getDatasets;