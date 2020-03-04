public abstract class Duck
{

	FlyBehavior flyBehavior;
	QuackBehavior quackBehavior;

	public Duck() {}
	public abstract void display();
	public void performFly() 		{ flyBehavior.fly(); }
	public void perform Quack() 	{ quackBehavior.quack(); }
	public void swim() 				{ System.out.println("All duckys float, mother ducker\n"); }

}