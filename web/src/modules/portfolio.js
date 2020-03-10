import React from 'react';
import { Table } from 'antd';
import matrix from './matrix.png';
import portfolioStrategies from './actions/portfolioStrategies';

class Overview extends React.Component {
	constructor(props){
		super(props);
		this.state = {
			load: false,
			dataSource: [],
				columns: [
				  {
				    title: 'Strategy',
				    dataIndex: 'strategy',
				    key: 'strategy',
				  },
				  {
				    title: 'Return',
				    dataIndex: 'return',
				    key: 'return',
				  },
				  {
				    title: '% Return',
				    dataIndex: 'perc_return',
				    key: 'perc_return',
				  },
				  {
				    title: 'Str Dev',
				    dataIndex: 'str_dev',
				    key: 'str_dev',
				  },
				  {
				    title: 'Sharpe',
				    dataIndex: 'sharpe',
				    key: 'sharpe',
				  }
				]
		}
	}

	componentDidMount(){
		this.props.updateKey('1')
		let portfolio = [];
		portfolioStrategies()
			.then(response => {
				response.strategies.map((strategy_data, index) => {
					portfolio.push({
						key: index,
						strategy: strategy_data.strategy_name,
						perc_return: strategy_data.strategy_return,
						sharpe: strategy_data.sharpe_ratio,
						return: strategy_data.equity_final
					})
				})
				this.setState({dataSource: portfolio})	
			})
			this.setState({load: true})
	}

	render(){
		return(
			<React.Fragment>
				<h1 style={{ color: '#ffffff'}}>Portfolio</h1>
				<div className="overview-container">
					{this.state.load && 
						<React.Fragment>
							<Table dataSource={this.state.dataSource} columns={this.state.columns} />
							<img src={matrix} />
						</React.Fragment>
					}
				</div>

			</React.Fragment>
		)
	}
}

export default Overview;
