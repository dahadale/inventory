import React, { useState, useEffect } from 'react';

const Login = () =>  {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [role, setRole] = useState('');
    const [errors, setErrors] = useState(false);
    const [loading, setLoading] = useState(true);


    useEffect(() => {
        if (localStorage.getItem('token') !== null) {
            window.location.replace('http://localhost:3000/dashboard');
        } else {
            setLoading(false);
        }
    }, []);

    const onSubmit = e => {
        e.preventDefault();

        const user = {
            email: email,
            password: password,
            role: role
        };

        fetch('http://localhost:8000/api/v1/users/auth/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        })
            .then(res => res.json())
            .then(data => {
                if (data.key) {
                    localStorage.clear();
                    localStorage.setItem('token', data.key);
                    localStorage.setItem('role', user.role);

                    if (localStorage.getItem('role') === 'entrenamiento') {
                        window.location.replace('http://localhost:3000/request');
                    } else if (localStorage.getItem('role') === 'logistica') {
                        window.location.replace('http://localhost:3000/delivery');
                    }
                    else {
                        window.location.replace('http://localhost:3000/login');
                    }
                } else {
                    setEmail('');
                    setPassword('');
                    setPassword('');
                    localStorage.clear();
                    setErrors(true);
                }
            });

    };

    return (
        <div>
            {loading === false && <h1>Login</h1>}
            {errors === true && <h2>Cannot log in with provided credentials</h2>}
            {loading === false && (
                <form onSubmit={onSubmit}>
                    <label htmlFor='email'>Email address:</label><br />
                    <input
                        name='email'
                        type='email'
                        value={email}
                        required
                        onChange={e => setEmail(e.target.value)}
                        />{' '}
                        <br />
                        <label htmlFor='password'>Password:</label><br />
                        <input
                        name='password'
                        type='password'
                        value={password}
                        required
                        onChange={e => setPassword(e.target.value)}
                        />{' '}



                        <select 
                        name="role"
                        onChange={e => setRole(e.target.value)} 
                        onBlur={e => setRole(e.target.value)} 
                        value={role}
                        default="entrenamiento"
                        >
                            <option value="-">---</option>
                            <option value="logistica">Logística</option>
                            <option value="entrenamiento" >Entrenamiento</option>
                        </select>
                        <br />
                        <input type='submit' value='Login' />
                </form>
            )}
        </div>
    );

};

export default Login;