import React, { useState, useEffect, Fragment } from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
    const [isAuth, setIsAuth] = useState(false);

    useEffect(() => {
        if (localStorage.getItem('token') !== null ) {
            setIsAuth(true);
        }
    }, []);

    return (

    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <Link className="navbar-brand" to='/dashboard'>Dashboard</Link>
    
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
        <li class="nav-item active">
            <Link className="nav-link" to='/delivery'>Order Alert</Link>
        </li>
        <li class="nav-item">
            <Link className="nav-link" to='/entry'>Entry</Link>
        </li>
        <li class="nav-item">
            <Link className="nav-link" to='/logout'>Search</Link>

        </li>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            Session
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <Link to='/logout'>Logout</Link>
            </div>
        </li>
        </ul>
    </div>
    </nav>
        

        
    );


};

export default Navbar;

