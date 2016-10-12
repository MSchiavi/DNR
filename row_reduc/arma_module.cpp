#include <iostream>
#include <vector>
#include <iostream>
#include <armadillo>
#include <math.h>
#include <time.h>
#include <typeinfo>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/list.hpp>
#include <boost/python/extract.hpp>
using namespace std;
using namespace arma;

/*void say_hello(const char* name) {
    cout << "Hello " <<  name << "!\n";
}
 */

boost::python::list ltv(boost::python::list Mat,int cols) {
    
    // arma stuff
    
    cout << "Armadillo version: " << arma_version::as_string() << endl;
    
    clock_t t1,t2;
    t1 = clock();
    
    mat G;
    
    G << 2 << -4 << 5 << -2 << 2 << -3 <<  -2 << 2 << -3 << endr
    << 4 << -1 << 0 << 2 << -4 << 5 <<  -2 << 2 << -3 << endr
    << -2 << 2 << -3 << 2 << -4 << 5 <<  -2 << 2 << -3 << endr
    <<  -8 << 2 << -11 << -2 << 2 << -3 << 32 << 91 << 304 << endr
    << 5 << 32 << 55 << 67 << 824 << 451 << 1000 << 4 << -32 << endr
    << 64 << 33 << 90 << 543 << 123 << 1232 << 131 << -131 << -54 << endr
    << -931 << 78 << 98 << 21 << 32 << 45 << 888 << -99 << -54 << endr
    << 7 << -32 << 67 << 99 << 98 << 103 << 43 << 54 << 88 << endr
    << -32 << -4 << -9 << 10 << 133 << 43 << 88 << 103 << 32 << endr;
    mat H;
    
    H << -33 << endr
    << -5 << endr
    << 19 << endr
    << 44 << endr
    << 68 << endr
    << 91 << endr
    << 71 << endr
    << 5 << endr
    << 23 << endr;
    mat X;
    
    X = solve(G,H);
    t2 = clock();
  //  X.print("X:");
    

    
    //Creating arrays
    double v[5] = {1, 1, 1, 1, 1};
    double c[5] = {2, 2, 2, 2, 2};
    
    // copying the arrays into matrix object for armadillo
    mat v_Copy(v, 1, 5);
    
    mat c_Copy(c, 1, 5);
    
    v_Copy.print("v_copy:");
    c_Copy.print("c_copy:");
    //inserting the c matrix AFTER row 1.
    v_Copy.insert_rows(1,c_Copy);
    
    v_Copy.print("v after insert");
    //mat A(hi,9,9);
    
    
    
    
    cout << "potato" << endl;
    cout << cols << endl;
    double temp_row[cols];
    for (int i = 0; i < cols  ; i++){
        temp_row[i] = static_cast<double>(boost::python::extract<u8>(Mat[i]));
    }
    cout << temp_row[0] << endl;
    
    /*
     mat B = { 1, 2, 3, 4, 5, 6 };
     B.reshape(2,3);
     B.print("B:");
     */
    
    //Test stuff
    
    
    
    
  /*  int row_count = boost::python::extract<int>(Mat.attr("__len__")());
    for(int i = 0; i<row_count; i++){
        cout << boost::python::extract<double>(Mat[i]) << endl;
    }
    int column_count = boost::python::extract<int>(Mat[1].attr("__len__")());
   
    
    cout << "ayeeeee" << endl;
    cout << row_count << endl;
    cout << column_count << endl;
    
    double my_row_a[row_count][column_count];
    

    
    for (int i=0; i<row_count; i++) {
        for(int j = 0; j <column_count; j++){
        my_row_a[i][j] = boost::python::extract<double>(Mat[i][j]);
        }
    }
    */
    /*mat my_row_a_copy(my_row_a,1,5);
    
    my_row_a_copy.print("my_row_a_copy");
    
    v_Copy.insert_rows(2,my_row_a_copy);
    
    v_Copy.print("v after python list");
    
    
    
    boost::python::list output;
    
    for (int i=0; i<row_length; i++){
        output.append(my_row_a[i]);
    }
    */
    
    // time stuff
    float diff ((float)t2-(float)t1);
    float seconds = diff / CLOCKS_PER_SEC;
    
    
    
    cout<<"time:"<<seconds<<endl;
    // end of time stuff
    
    return Mat;
    
}


/*BOOST_PYTHON_MODULE(hello)
{
    def("say_hello", say_hello);
}
*/


using namespace boost::python;
BOOST_PYTHON_MODULE(arma_mod)
{
    def("ltv",ltv);
}
