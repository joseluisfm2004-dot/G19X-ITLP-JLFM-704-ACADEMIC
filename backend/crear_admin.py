import asyncio
import os
import logging
from sqlalchemy.future import select
from app.db.database import AsyncSessionLocal
from app.models.models import Usuario
from app.core.security import get_password_hash

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

async def crear_administrador():
    logger.info("=== Crear Primer Usuario Administrador ===")
    nombre = input("Nombre completo: ")
    email = input("Correo electrónico: ")
    password = input("Contraseña (mínimo 6 caracteres): ")

    if len(password) < 6:
        logger.error("Error: La contraseña es muy corta.")
        return

    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Usuario).where(Usuario.email == email))
        if result.scalars().first():
            logger.error("Error: Ya existe un usuario con este correo electrónico.")
            return

        hashed_pwd = get_password_hash(password)
        nuevo_admin = Usuario(
            nombre=nombre,
            email=email,
            password_hash=hashed_pwd,
            rol="admin"
        )
        db.add(nuevo_admin)
        await db.commit()
        logger.info(f"\n¡Éxito! El administrador '{nombre}' ({email}) fue creado correctamente.")
        logger.info("Ya puedes iniciar sesión en el sistema.")

if __name__ == "__main__":
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(crear_administrador())