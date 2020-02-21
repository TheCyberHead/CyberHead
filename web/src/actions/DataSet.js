async function getDatasets(){
	let response = await fetch('http://localhost:5000/datasets')
	let data = await response.json()
	return data
}


export default getDatasets;