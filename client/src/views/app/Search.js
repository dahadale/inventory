import React, { useState, useEffect, Fragment } from 'react';

const Search = () => {

  return (
    <div className="container">
        <div className="row " >
            <div className="col-md-8   mt-5">
                <div class="card w-100">
                    <div class="card-body">


                    <form>
                    <div className="form-row mb-3">
                        <div className="col-7">
                            <input type="text" class="form-control" placeholder="Part Number">
                            </input>
                        </div>
                        <div className="col-3">
                            <button type="submit" class="btn btn-primary">Search</button>
                        </div>
                    </div>
                    </form>

                    <table class="table">
                <thead>
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col">Part Number</th>
                    <th scope="col">Item Name</th>
                    <th scope="col">Location</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Name Instructor</th>
                    <th scope="col">Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                    <th scope="row">1</th>
                    <td>Mark</td>
                    <td>Otto</td>
                    <td>@mdo</td>
                    <td>@mdo</td>
                    <td>@mdo</td>
                    <td>@mdo</td>
                    </tr>
                    <tr>
                    <th scope="row">2</th>
                    <td>Jacob</td>
                    <td>Thornton</td>
                    <td>@fat</td>
                    <td>@fat</td>
                    <td>@fat</td>
                    <td>@fat</td>

                    </tr>
                    <tr>
                    <th scope="row">3</th>
                    <td>Larry</td>
                    <td>the Bird</td>
                    <td>@twitter</td>
                    <td>@twitter</td>
                    <td>@twitter</td>
                    <td>@twitter</td>
                    </tr>
                </tbody>
                </table>



                    </div>
                </div>
            </div>


            <div className="col-md-4   mt-5">
                <div class="card w-100">
                    <div class="card-body d-flex justify-content-center">
                        {/* <h5 class="card-title text-center">Request</h5> */}


                        <div className="d-flex justify-content-center">
                            <img src="data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%22200%22%20height%3D%22200%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%20200%20200%22%20preserveAspectRatio%3D%22none%22%3E%3Cdefs%3E%3Cstyle%20type%3D%22text%2Fcss%22%3E%23holder_17ac033805c%20text%20%7B%20fill%3Argba(255%2C255%2C255%2C.75)%3Bfont-weight%3Anormal%3Bfont-family%3AHelvetica%2C%20monospace%3Bfont-size%3A10pt%20%7D%20%3C%2Fstyle%3E%3C%2Fdefs%3E%3Cg%20id%3D%22holder_17ac033805c%22%3E%3Crect%20width%3D%22200%22%20height%3D%22200%22%20fill%3D%22%23777%22%3E%3C%2Frect%3E%3Cg%3E%3Ctext%20x%3D%2274.421875%22%20y%3D%22104.65%22%3E200x200%3C%2Ftext%3E%3C%2Fg%3E%3C%2Fg%3E%3C%2Fsvg%3E" 
                            alt="..." class="img-thumbnail"></img>
                        </div>


                    </div>
                </div>
            </div>



        </div>            
    </div>
  );
};

export default Search;