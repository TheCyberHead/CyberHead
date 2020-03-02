import API_BASE from './URL'

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


export default createDataSet;