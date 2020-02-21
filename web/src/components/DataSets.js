import React from 'react';
import { Form, Radio, Input, Modal, Card, Col, Row, Button } from 'antd';
import {Line} from 'react-chartjs-2';
import getDatasets from '../actions/DataSet';

const data = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'Coffee',
      fill: false,
      lineTension: 0.1,
      backgroundColor: 'rgba(75,192,192,0.4)',
      borderColor: 'rgba(187,0,73,0.6)',
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: 'rgba(75,192,192,1)',
      pointBackgroundColor: '#fff',
      pointBorderWidth: 1,
      pointHoverRadius: 2,
      pointHoverBackgroundColor: 'rgba(75,192,192,1)',
      pointHoverBorderColor: 'rgba(220,220,220,1)',
      pointHoverBorderWidth: 1,
      pointRadius: 0,
      pointHitRadius: 10,
      data: [65, 59, 80, 81, 56, 55, 40]
    }
  ]
};


class DataSets extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			datasets: [],
			load: true,
			openModal: false
		}
		this.triggerOpenModal = this.triggerOpenModal.bind(this)
	}

	componentDidMount(){
		this.props.updateKey('5')
		getDatasets()
			.then(response => this.setState({datasets: response.datasets}))
	}

	triggerOpenModal(){
		this.setState({openModal: !this.state.openModal})
	}

	render(){
		return(
			<React.Fragment>
				<Modal
          title="Add a new data set"
          visible={this.state.openModal}
          onOk={this.handleOk}
          onCancel={this.triggerOpenModal}
        >
          <Form layout="horizontal">
            <Form.Item>
              <Input placeholder="Identifier" />
            </Form.Item>
            <Form.Item>
              <Input placeholder="Reference Symbol" />
            </Form.Item>

            <Form.Item>
              <Input placeholder="Description" />
            </Form.Item>

            <Form.Item>
              <Input placeholder="Source" />
            </Form.Item>
            <Form.Item>
              <Button type="primary">Submit</Button>
            </Form.Item>
          </Form>
        </Modal>

        <Modal
          title="Upload Data Set"
          visible={this.state.uploadDataSet}
          onOk={this.handleOk}
          onCancel={this.uploadDataSetModal}
        >
          <p>Some contents...</p>
        </Modal>


				<h1 style={{ color: '#ffffff'}}>Data Sets</h1>
				<div style={{ padding: '30px'}} className="dataset-box">

						<Button type="primary" icon="file-add" size="large" onClick={this.triggerOpenModal} style={{marginRight: '1em'}}>
		          Import data set
		        </Button>

		        <Button type="primary"  icon="file-add" size="large">
		          Subscribe from source
		        </Button>
				    <Row gutter={16} style={{marginTop:'1em'}}>
				    {this.state.load && this.state.datasets.map(dataset => (
				    	<Col span={8}>
				    	  <Card key={dataset.id} title={dataset.identifier} bordered={true} className="dataset-card">
				    	    <p>{dataset.description}</p>
				    	    <p><strong>Symbol</strong>: {dataset.reference_symbol}</p>
				    	  </Card>
				    	</Col>
				    ))}
				    </Row>					
				    <Line data={data} />
				  </div>
			</React.Fragment>
		)
	}
}

export default DataSets;