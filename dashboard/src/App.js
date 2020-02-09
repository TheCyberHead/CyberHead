import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { Layout, Menu, Icon } from 'antd';
import './App.css';
import Strategies from './components/Strategies';
import Overview from './components/Overview';
import HeatVision from './components/HeatVision';
import DataSets from './components/DataSets';
import Configuration from './components/Configuration';

const { Header, Sider, Content } = Layout;

class App extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      collapsed: false,
      selectedKeyMenu: "1"
    };
    this.updateMenuKey = this.updateMenuKey.bind(this);
    this.menuItemClick = this.menuItemClick.bind(this);
  }

  updateMenuKey(key){
    this.setState({selectedKeyMenu: key})
    console.log('updated')
  }

  menuItemClick(ev){
    const menu = {
      1: 'overview',
      2: 'strategies',
      3: 'heat-vision',
      4: 'configuration',
      5: 'dataSets'
    }
    console.log(menu[ev.key])
  }

  toggle = () => {
    this.setState({
      collapsed: !this.state.collapsed,
    });
  };

  render() {
    return (
      <Layout>
        <Sider trigger={null} collapsible collapsed={this.state.collapsed}>
          <div className="logo" />
          <Menu theme="dark" mode="inline" defaultSelectedKeys={["1"]} selectedKeys={[this.state.selectedKeyMenu]}>
            <Menu.Item key="1" onClick={this.menuItemClick} >
              <Icon type="user" />
              <span>Overview</span>
            </Menu.Item>
            <Menu.Item key="2" onClick={this.menuItemClick} >
              <Icon type="stock" />
              <span>Strategies</span>
            </Menu.Item>
            <Menu.Item key="3" onClick={this.menuItemClick} >
              <Icon type="dot-chart" />
              <span>Heat Vision</span>
            </Menu.Item>

            <Menu.Item key="4" onClick={this.menuItemClick}>
              <Icon type="experiment" />
              <span>Configuration</span>
            </Menu.Item>

            <Menu.Item key="5" onClick={this.menuItemClick}>
              <Icon type="file-add" />
              <span>DataSets</span>
            </Menu.Item>
          </Menu>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', padding: 0 }}>
            <Icon
              className="trigger"
              type={this.state.collapsed ? 'menu-unfold' : 'menu-fold'}
              onClick={this.toggle}
            />
          </Header>
          <Content
            style={{
              margin: '24px 16px',
              padding: 24,
              background: '#fff',
              minHeight: '100vh',
            }}
          >
            <Router>
              <Switch>
                <Route path="/strategies">
                  <Strategies updateKey={this.updateMenuKey} />
                </Route>

                <Route path="/heat-vision">
                  <HeatVision updateKey={this.updateMenuKey} />
                </Route>

                <Route path="/datasets">
                  <DataSets updateKey={this.updateMenuKey} />
                </Route>

                <Route path="/configuration">
                  <Configuration updateKey={this.updateMenuKey} />
                </Route>

                <Route path="/">
                  <Overview updateKey={this.updateMenuKey} />
                </Route>
              </Switch>
            </Router>
          </Content>
        </Layout>
      </Layout>
    );
  }
}

export default App;