#include <iostream>
#include <string>
#include <vector>
#include <armadillo>
#include <math.h>
#include <time.h>
#include <typeinfo>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>
#include <boost/python/extract.hpp>
#include <boost/python.hpp>
using namespace std;
using namespace arma;

/*struct World {
    
    
    
     World(std::string msg): msg(msg) {}
     void set(std::string msg) { this->msg = msg; }
     std::string greet() { return msg; }
  
 std::string msg;
*/

class Potato {
    
    private:
    
   

    public:
    string a;
    mat Main_Matrix;
    mat Solution;
    boost::python::list row_f;
    int cols_f;
    int count_rows;
        Potato(boost::python::list f_row,int f_cols){
            row_f = f_row;
            cols_f = f_cols;
        cout << "Armadillo version: " << arma_version::as_string() << endl;
        
       
    
        
    }
    // creates a temporary array and inserts it into the matrix
    void start(){
        double temp_row[cols_f];
        
        for (int i = 0; i < cols_f  ; i++){
            temp_row[i] = static_cast<double>(boost::python::extract<u8>(row_f[i]));
        }
        mat t(temp_row,1,cols_f);
        Main_Matrix.insert_rows(0,t);
        count_rows = 1;
        t.reset();

        
    }
    //adds a row into the last position
    void addrow(boost::python::list row,int cols){
       
        double temp_row[cols];
        
        for (int i = 0; i < cols  ; i++){
            temp_row[i] = static_cast<double>(boost::python::extract<u8>(row[i]));
        }
        
        mat t(temp_row,1,cols);
        t.print("this is t at addrow");
        Main_Matrix.insert_rows(count_rows,t);
        
        Main_Matrix.print("ayeee after second insert");
        
        count_rows++;
        t.reset();
        
    }

    
    //inserts a column into the last position
    void addcol(boost::python::list col, int rows){
        double temp_col[rows];
        
        for (int i = 0; i < rows; i++){
            temp_col[i] = static_cast<double>(boost::python::extract<u8>(col[i]));
        }
        
        mat t(temp_col,rows,1);
        t.print("ayee its col T");
        Main_Matrix.insert_cols(Main_Matrix.n_cols,t);
        Main_Matrix.print("ayee I added a column");
        
        t.reset();
        
    }
    
    void set_solution(boost::python::list sol, int rows){
    double temp_sol[rows];
    
    for(int i = 0; i< rows; i++){
        temp_sol[i] = static_cast<double>(boost::python::extract<u8>(sol[i]));
        
    }
        mat t(temp_sol,rows,1);
        
    Solution.insert_cols(0,t);
        
    Solution.print("ayeee im the solution");
        t.reset();

}
    
    
     mat row_reduc(){
         mat X;
         
         X = solve(Main_Matrix,Solution,solve_opts::no_approx);
         X.print("I solved it mom");
         
         return X;
     
     }
     

};





using namespace boost::python;
BOOST_PYTHON_MODULE(arma_mod)
{
 /*
    class_<World>("World", init<std::string>())
    .def("greet", &World::greet)
    .def("set", &World::set)
    ;
    */
   
    class_<Potato>("Potato",init<boost::python::list,int>())
    .def("start", &Potato::start)
    .def("addrow", &Potato::addrow)
    .def("addcol", &Potato::addcol)
    .def("set_solution", &Potato::set_solution)
    .def("row_reduc", &Potato::row_reduc)
    //.def("getrow", &Potato::getrow)
     // .def(init<boost::python::list,int>())
    //.def("Matrix",Matrix)
    ;
}
