
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from './components/layout/Navbar'; // import navbar

import Login from './views/auth/Login';
import Signup from './views/auth/Signup';
import Logout from './views/auth/Logout';
import Dashboard from './views/app/Dashboard';
import Delivery from './views/app/Delivery';
import Request from './views/app/Request';
import Entry from './views/app/Entry';
import Search from './views/app/Search';

const App = () => {
  return (
    <div className='App'>
      <Router>
        <Navbar />
        <Switch>
          <Route path='/login' component={Login} exact />
          <Route path='/signup' component={Signup} exact />
          <Route path='/logout' component={Logout} exact />
          <Route path='/delivery' component={Delivery} exact />
          <Route path='/request' component={Request} exact />
          <Route path='/entry' component={Entry} exact />
          <Route path='/search' component={Search} exact />

          <Route path='/dashboard' component={Dashboard} exact />
        </Switch>
      </Router>
    </div>
  );
};

export default App;