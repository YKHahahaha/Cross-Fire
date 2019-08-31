#include <Python.h>
#include<iostream>

using namespace std;

int main()
{

    Py_Initialize();//使用python之前，要调用Py_Initialize();这个函数进行初始化
    if (!Py_IsInitialized())
    {
        printf("初始化失败！");
        return 0;
    }

    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");//这一步很重要，修改Python路径


    PyObject * pModule = NULL;//声明变量
    PyObject * pFunc = NULL;// 声明变量

    pModule = PyImport_ImportModule("pythonTest");//这里是要调用的文件名hello.py
    if (pModule == NULL)
    {
        cout << "没找到" << endl;
    }

    pFunc = PyObject_GetAttrString(pModule, "add_num");//这里是要调用的函数名
    PyObject* args = Py_BuildValue("(ii)", 28, 103);//给python函数参数赋值

    PyObject* pRet = PyObject_CallObject(pFunc, args);//调用函数

    int res = 0;
    PyArg_Parse(pRet, "i", &res);//转换返回类型

    cout << "res:" << res << endl;//输出结果

    Py_Finalize();//调用Py_Finalize，这个根Py_Initialize相对应的。

    return 0;
}
