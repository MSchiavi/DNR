#include <iostream>
#include <armadillo>
#include <Python.h>
#include <math.h>
#include <time.h>
#include <vector>
#include <typeinfo>

using namespace std;
using namespace arma;

void Solve()
{
    cout << "Armadillo version: " << arma_version::as_string() << endl;
    
    //cout <<"rows:" << rows << endl;
    //cout << "rows:" << typeid(rows).name() << endl;
    //cout << "cols" << cols << endl;
    //New stuff
    
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
    X.print("X:");
    
    //Creating arrays
    double v[5] = {1, 1, 1, 1, 1};
    
    double c[5] = {2, 2, 2, 2, 2};
    
    std::vector< double > arr;
    
    arr.push_back(2.0);
    arr.push_back(3.0);
    arr.push_back(3.0);
    arr.push_back(4.0);
    arr.push_back(5.0);
    
    double arrr[5] = {2,3,3,4,5};
    // copying the arrays into matrix object for armadillo
    mat v_Copy(v, 1, 5);
    
    mat c_Copy(c, 1, 5);
    
    
    mat arr_Copy(arr);
    
    v_Copy.print("v_copy:");
    c_Copy.print("c_copy:");
    arr_Copy.print("arr");
    
    //inserting the c matrix AFTER row 1.
    v_Copy.insert_rows(1,c_Copy);
    
    v_Copy.insert_rows(1,arr_Copy);
    
    v_Copy.print("v after insert");
    
    //mat A(hi,9,9);
    
    
    
    
    /*
     mat B = { 1, 2, 3, 4, 5, 6 };
     B.reshape(2,3);
     B.print("B:");
     */
    float diff ((float)t2-(float)t1);
    float seconds = diff / CLOCKS_PER_SEC;
    
    
    
    cout<<"time:"<<seconds<<endl;
    
}

int main(){
    
    Solve();
    
}

