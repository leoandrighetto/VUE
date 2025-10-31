<template>
    <div class="componente">
        <h1>Slots com Nome</h1>
        <button> <slot name="icone"/> <slot name="texto"/> </button>

        <!-- <button> 
            <slot name="texto"/> 
            <slot name="icone"/>
            Home
        
        </button> -->

    </div>
</template>