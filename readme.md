# Readme - Configuración de Proyecto en Odoo

Este readme proporciona una guía paso a paso para configurar un proyecto en Odoo utilizando Docker y un archivo docker-compose.yml.

---

## Pasos de Configuración:

1. **Clonar Repositorio:**
    Clona el repositorio de Odoo en tu máquina local.
    Creando un archivo docker compose.yml

2. **Ejecutar Docker:**
    Ejecuta Docker utilizando el siguiente comando:
    ```bash
    docker-compose up -d
    ```

3. **Acceder al Contenedor:**
    Accede al contenedor utilizando la siguiente línea de comandos. Recuerda cambiar `prcticaexam-web2_dev-1` por el nombre del contenedor requerido.
    ```bash
    docker exec -u root -it prcticaexam-web2_dev-1 /bin/bash
    ```

4. **Crear Extensión:**
    Dirígete a la carpeta de addons y crea una nueva extensión dentro del contenedor:
    ```bash
    cd /mnt/extra-addons
    odoo scaffold pruebaexamen/
    ```

5. **Permisos de Modificación:**
    Otorga permisos para modificar la extensión recién creada:
    ```bash
    chmod -R 777 pruebaexamen/
    ```

6. **Reiniciar Docker:**
    Reinicia Docker para aplicar los cambios:
    ```bash
    docker-compose restart
    ```
  
7. **Activar Addons en Odoo:**
    Activa los addons en Odoo buscándolos por el nombre especificado en el manifest.
![docker activo.png](IMAGENES%20SXE%2Fdocker%20activo.png)
8. **Crear Tabla en Models:**
    Define la estructura de la tabla en el archivo `models.py` como sigue:
    ```python
    from odoo import fields, models
    
    class TestModel(models.Model):
        _name = "test_model"  # Cambiar por el nombre deseado para la tabla
        _description = "Test Model"  # Cambiar por la descripción deseada
        
        name = fields.Char(string="Nombre")
        description = fields.Text(string="Descripción")
    ```

9. **Crear Datos:**
    Crea un archivo `datos.xml` dentro de la carpeta `datos` con el siguiente formato , para añadir 4 campos más se copia la estructura principal y
    se sustituye lo que hay entre comillas por el campo de la tabla que declaramos en remesa.py ademas de cambiar el id por ejemplo por
   examensxe.nombres2 , luego se le da valores.
   :
    ```xml
    <odoo>
    <data>
        <record model="remesa" id="examensxe.nombres"> #Cambiamos el model por el nombre de nuestra Tabla.
            # aquí rellenamos con los campos de la tabla que precisemos.
            # se sustituye lo que hay en comillas por el campo de la tabla que declaramos en remesa.py y luego se le da un valor.
            <field name="id">542387RT</field>
            <field name="producto">tomates</field>
            <field name="viabilidad">15</field>
        </record>
    </data>
    </odoo
    
      ![data xml.png](IMAGENES%20SXE%2Fdata%20xml.png)
    ```

10. **Configurar Seguridad:**
    En la carpeta `security`, edita el archivo `ir.model.access.csv` para configurar los permisos
    de acceso a la tabla. Reemplaza `access_examensxe_examensxeAQUI 2 AQUI` por el nombre de la tabla.


11. **Actualizar Referencia de Tablas:**
    En el archivo `__init__.py` dentro de la carpeta `models`, agrega una referencia a tu tabla:
    ```python
    from . import remesa
    ```

12. **Configurar Vistas:**
    En el archivo `views.xml`, configura las vistas de acuerdo a tus modelos , campos y se esconde el id.
 ```xml
    <record model="ir.ui.view" id="examensxe.list">
      <field name="name">examensxe list</field>
      <field name="model">remesa</field>
      <field name="arch" type="xml">
        <tree>

          <field name="producto"/>
          <field name="viabilidad"/>
        </tree>
      </field>
    </record>
```
```xml
    <!-- actions opening views on models -->

    <record model="ir.actions.act_window" id="examensxe.action_window">
      <field name="name">examensxe window</field>
      <field name="res_model">remesa</field>
      <field name="view_mode">tree,form</field>
    </record>
```

![docker 2.png](IMAGENES%20SXE%2Fdocker%202.png)

13. **Actualizar Menús:**

    Edita los menús en el archivo `views.xml` , en el archivo `manifest.xml` para vincularlos correctamente y que así
    se puedan modificar posteriormente.

![docker 3.png](IMAGENES%20SXE%2Fdocker%203.png)
![docker 4.png](IMAGENES%20SXE%2Fdocker%204.png)
![docker 5.png](IMAGENES%20SXE%2Fdocker%205.png)
---
 
**Y con esto estaría todo levantado**   
    
