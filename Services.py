    public static void  elUsuarioSeEncuentraEnLaPantallaDeHome() {
        navigateTo(PropertyManager.getProperty("http://automationpractice.com/index.php"));
		
    }
	public static void elUsuarioHaceClickEnElBotónDresses() {
        click(ProductosEnElCarritoConstants.DRESSES_BUTTON_XPATH);
		   }
	public static void elUsuarioHaceClickEnLaOpciónEveningDresses() {
        click(ProductosEnElCarritoConstants.DVENINGDRESSES_BUTTON_XPATH);
		   }
		   
	public static void elUsuarioHaceClickBtónAddToCart() {
        click(ProductosEnElCarritoConstants.ADDTOCART_BUTTON_XPATH);
		   }
	public static void elUsuarioHaceClickBtónX() {
        click(ProductosEnElCarritoConstants.CLICK_BUTTON_X_XPATH);
		   }
	public static void elUsuarioVisualizaElProductoSeleccionado(){
       waitVisibility(ProductosEnElCarritoConstants.CLICK_CART_XPATH);
        }
	public static void comprobarQueElVestidoSeaElQueSeleccionamosPreviamente() {
        click(ProductosEnElCarritoConstants.CLICK_CART_XPATH);
		waitVisibility(ProductosEnElCarritoConstants.DETAIL_XPATH);
        }
		
		
