#include <iostream>
using namespace std;



class UAV {
	private:
	String _name;
	bool _is_landing;
	bool _is_takeoff;
	
	public:
	UAV(){
		_is_landing = false;
		_is_takeoff = false;
	}
	bool takeoff(){
		return
	}
	
		
	
}

class Drone : public UAV {
	
	
	public:
	UAV(String name){
		_name = name
	}
	
	bool takeoff(){
		if(_is_landing == true)
			return false;
		else{
			_is_takeoff = true;
			return _is_takeoff;
		}
			
	}
}

int main() 
{
    cout << "Hello, World!";
    return 0;
}