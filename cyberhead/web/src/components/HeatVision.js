import React from 'react';
import {Form,Input, Button} from 'antd';
import submitHeatmap from '../actions/submitHeatmap';
import getHeatMaps from '../actions/getHeatMaps';
import getHeatMapData from '../actions/getHeatMapData';

class HeatVision extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: false,
			file64: '',
			heatmaps: [],
			selectedHeatMap: [],
			heatmapLoaded: false
		}
	}

	componentDidMount(){
		this.props.updateKey('3')
		this.listHeatMaps()
	}

	fileChange = ev => {
		let reader = new FileReader();
		reader.readAsDataURL(ev.target.files[0])
		reader.onload = () => {
			this.setState({file64: reader.result})
		}
	}

	submitForm = ev => {
		ev.preventDefault()
		const {title, file64} = this.state
		const heatmap = {heatmap: {title, file64}}
		submitHeatmap(heatmap)
			.then(response => console.log(response))
		console.log(file64)
	}

	handleChange = ev => {
		const {name, value} = ev.target
		this.setState({[name]: value})
	}

	loadHeatmap = ev => {
		const heatmap_id = ev.target.dataset.heatmap
		const currentHeatMap = this.state.heatmaps.filter(heatmap => heatmap['id'] == heatmap_id)
		this.setState({selectedHeatMap: currentHeatMap})
		if (this.state.selectedHeatMap != []) {
			this.setState({heatmapLoaded: true})
		}
		console.log(currentHeatMap)
	}

	listHeatMaps = () => {
		getHeatMaps()
			.then(response => this.setState({heatmaps: response.heatmaps}))
		this.setState({load: !this.state.load})
	}

	render(){
		return(
			<div>
				<h1 style={{ color: '#ffffff'}}>Heat Vision</h1>
				<div className="heatvision-box">

				<div className="heat-vision">
				<h3>Create a heat map</h3>
				<Form layout="horizontal" className="heatmap-upload-form" onSubmit={this.submitForm}>
					<Form.Item>
						<Input placeholder="Heat Map Identificator" name="title" onChange={this.handleChange}/>
					</Form.Item>

					<Form.Item>
						<input type="file" onChange={this.fileChange} className="heat-upload-file"/>
					</Form.Item>

					<Form.Item>
					  <Button type="primary" htmlType="submit">Upload</Button>
					</Form.Item>
				</Form>
				<div className="heatmap-list">
					<ul>
						{this.state.load && this.state.heatmaps.map(heatmap => (
							<li data-heatmap={heatmap.id} key={heatmap.id} onClick={this.loadHeatmap}>{heatmap.title}</li>
						))}
					</ul>
				</div>
				</div>
					{!this.state.heatmapLoaded && (
						<div className="loader">Loading...</div>
					)}
					
					{this.state.heatmapLoaded && (
						<div className="heatmap-box-information">
							<h1>{this.state.selectedHeatMap[0].title}</h1>
							<img src={`http://localhost:5000/get_heatmap/${this.state.selectedHeatMap[0].image_encoded.replace('tmp/images/', '')}`}/>
						</div>
					)}
				</div>
			</div>
		)
	}
}

export default HeatVision;