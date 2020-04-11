import API_BASE from './URL'

async function getDatasets(){
	let response = await fetch(`${API_BASE}/datasets`)
	let data = await response.json()
	return data
}

async function createDataSet(dataset){
	let response = await fetch(`${API_BASE}/datasets`,{
			method: 'POST',
			body: JSON.stringify(dataset),
			headers:{
				'Content-Type': 'application/json'
			}
		})
	let data = await response.json()
	return data
}


export { getDatasets, createDataSet };