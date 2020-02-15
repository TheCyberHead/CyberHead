import React from 'react';
import { Card, Col, Row } from 'antd';

class DataSets extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: true
		}
	}

	componentDidMount(){
		this.props.updateKey('5')
	}

	render(){
		return(
			<React.Fragment>
				<h1 style={{ color: '#ffffff'}}>Data Sets</h1>
				<hr/>

				<div style={{ padding: '30px' }}>
				    <Row gutter={16}>
				      <Col span={8}>
				        <Card title="EUR/USD" bordered={true} style={{'background-color': "#9E9E9E"}} >
				          From : 01-01-2018
				          <br/>
				          To : From : 01-01-2020
				        </Card>
				      </Col>
				      <Col span={8}>
				        <Card title="USD/JPY" bordered={false}>
				          From : 17-03-2018
				          <br/>
				          To : From : 14-02-2020
				        </Card>
				      </Col>
				      <Col span={8}>
				        <Card title="Historical Price Coffee 3" bordered={false}>
				          From : 01-10-2019
				          <br/>
				          To : From : 18-11-2019
				        </Card>
				      </Col>
				    </Row>
				  </div>


				  <img style={{width: '80%', 'margin-left': '7em'}} src="https://cyberhead.s3.amazonaws.com/Screen+Shot+2020-02-14+at+22.31.03.png" />
			</React.Fragment>
		)
	}
}

export default DataSets;