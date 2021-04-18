
class StarButtsCoffee {
    public static void main(String args[])
    {
        System.out.println("**************************************");
        System.out.println("Hello and Welcome to StarButts Coffee!");
        System.out.println("**************************************");
        System.out.println("What do the fuckers want?");
        
        System.out.println("Espresso");
        Beverage beverage = new Espresso();
        System.out.println(beverage.getDescription() + " $" + beverage.cost());
        
        System.out.println("Double Mocha House Blend");
        Beverage beverage2 = new HouseBlend();
        beverage2 = new Mocha(beverage2);
        beverage2 = new Mocha(beverage2);
        System.out.println(beverage2.getDescription() + " $" + beverage2.cost());
        
        System.out.println("Soy Mocha House Blend with Whipped Cream");
        Beverage beverage3 = new HouseBlend();
        beverage3 = new Soy(beverage3);
        beverage3 = new Mocha(beverage3);
        beverage3 = new Whip(beverage3);
        System.out.println(beverage3.getDescription() + " $" + beverage3.cost());
        
    }
}