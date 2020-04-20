import React from 'react';
import { Table } from 'antd';
import portfolioStrategies from '../actions/portfolioStrategies';

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
				    title: 'Final Equity',
				    dataIndex: 'return',
				    key: 'return',
				  },
				  {
				    title: 'Return (%)',
				    dataIndex: 'perc_return',
				    key: 'perc_return',
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
						perc_return: parseFloat(strategy_data.strategy_return).toFixed(2),
						sharpe: parseFloat(strategy_data.sharpe_ratio).toFixed(3),
						return: `${parseFloat(strategy_data.equity_final).toFixed(3)} USD`
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
						</React.Fragment>
					}
				</div>

			</React.Fragment>
		)
	}
}

export default Overview;
