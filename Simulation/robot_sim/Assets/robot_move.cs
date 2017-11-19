using UnityEngine;
using System.Collections;
using System.Collections.Generic;
public class robot_move : MonoBehaviour {
	public Vector3 newLoc;
    public float speed = 10f;
    public Transform robot;
    public float movetime;
    
	// Update is called once per frame
	void Update () {
        
	}
	
	public void forceMove(){

		
        StartCoroutine(MoveToPosition(robot, newLoc, movetime));

	}
	public void moveUp(float upspeed){
		transform.Translate(new Vector3(0,0,upspeed * Time.deltaTime));
	}
	public void moveDown(float downspeed){
		transform.Translate(new Vector3(0,0,-downspeed * Time.deltaTime));
	}
	public void moveLeft(float leftspeed){
		transform.Translate(new Vector3(-leftspeed * Time.deltaTime,0,0));
	}
	public void moveRight(float rightspeed){
		transform.Translate(new Vector3(rightspeed * Time.deltaTime,0,0));
	}

	public IEnumerator MoveToPosition(Transform transform, Vector3 position, float timeToMove)
    {
      var currentPos = transform.position;
      var t = 0f;
       while(t < 1)
       {
             t += Time.deltaTime / timeToMove;
             transform.position = Vector3.Lerp(currentPos, position, t);
             yield return null;
      }
    }
}