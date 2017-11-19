using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class robot_input : MonoBehaviour {
	
    public float speed = 10f;
    //public Transform robot;
    //public float movetime;
	// Use this for initialization
	void Start () {
		
		
	}
	public void checkInput(){
		Vector3 pos = transform.position;

        if (Input.GetKey("w") )
        {
            
            //pos.y += panSpeed * Time.deltaTime;
            //Debug.Log(Time.deltaTime);
            //moveUp(speed);
            robot_move sn = gameObject.GetComponent<robot_move>();
            sn.moveUp(speed);
            
        }
        if (Input.GetKey("s"))
        {
            //pos.y -= panSpeed * Time.deltaTime;
            robot_move sn = gameObject.GetComponent<robot_move>();
            sn.moveDown(speed);
        }
        if (Input.GetKey("d"))
        {
            //pos.x += panSpeed * Time.deltaTime;
            robot_move sn = gameObject.GetComponent<robot_move>();
            sn.moveRight(speed);
        }
        if (Input.GetKey("a"))
        {
        	robot_move sn = gameObject.GetComponent<robot_move>();
            sn.moveLeft(speed);
            //pos.x -= panSpeed * Time.deltaTime;
        }

        if (Input.GetKey("m")){
        	robot_move sn = gameObject.GetComponent<robot_move>();
        	sn.forceMove();
        }
	}
	// Update is called once per frame
	void Update () {
		checkInput();
	}
	
}
