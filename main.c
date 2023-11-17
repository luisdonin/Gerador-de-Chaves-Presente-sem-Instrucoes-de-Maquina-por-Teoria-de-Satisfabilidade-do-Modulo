#include <gtk/gtk.h>
#include <string.h>

int valida(int valCode[5]) {
    int sum = valCode[0] + valCode[1] + valCode[2] + valCode[3] + valCode[4];
    return sum % 2 == 0;
}

void on_button_clicked(GtkWidget *button, gpointer user_data) {
    GtkEntry *entry = (GtkEntry *)user_data;
    const char *text = gtk_entry_get_text(entry);
    int valCode[5];
    for (int i = 0; i < 5 && i < strlen(text); i++) {
        valCode[i] = text[i] - '0';
    }
    if (valida(valCode)) {
        gtk_button_set_label(GTK_BUTTON(button), "Senha valida!");
    } else {
        gtk_button_set_label(GTK_BUTTON(button), "Senha invalida!");
    }
}

void on_reset_clicked(GtkWidget *button, gpointer user_data) {
    GtkWidget **widgets = (GtkWidget **)user_data;
    GtkEntry *entry = GTK_ENTRY(widgets[0]);
    GtkWidget *validate_button = widgets[1];
    gtk_entry_set_text(entry, "");
    gtk_button_set_label(GTK_BUTTON(validate_button), "Validar senha");
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Main");
    gtk_window_set_default_size(GTK_WINDOW(window), 800, 600);
    GtkWidget *box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(window), box);

    GtkEntry *entry = GTK_ENTRY(gtk_entry_new());
    gtk_box_pack_start(GTK_BOX(box), GTK_WIDGET(entry), TRUE, TRUE, 0);

    GtkWidget *button = gtk_button_new_with_label("Digite a senha");
    g_signal_connect(button, "clicked", G_CALLBACK(on_button_clicked), entry);
    gtk_box_pack_start(GTK_BOX(box), button, TRUE, TRUE, 0);

    GtkWidget *widgets[2] = {GTK_WIDGET(entry), button};
    GtkWidget *reset_button = gtk_button_new_with_label("Testar outra senha");
    g_signal_connect(reset_button, "clicked", G_CALLBACK(on_reset_clicked), widgets);
    gtk_box_pack_start(GTK_BOX(box), reset_button, TRUE, TRUE, 0);

    gtk_widget_show_all(window);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    gtk_main();

    return 0;
}