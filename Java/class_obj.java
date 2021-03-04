class Student{
	public int age;
	Student(int age){
		this.age = age;
	}
}

class Main{
	public void changeAge(Student obj){
		obj.age = 40;
	}
	public static void main(String[] args){
		Main new_obj = new Main();
		Student student = new Student(30);
		System.out.println(student.age);
		new_obj.changeAge(student);
		System.out.println(student.age);
	}
}
